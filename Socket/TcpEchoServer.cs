using System;
using System.Net;
using System.Net.Sockets;

class TcpEchoServer
{
    private const int BUFFSIZE = 32;


    static void Main(string[] args)
    {
        if (args.Length > 1)
        {
            throw new ArgumentException("Parameters: [<Port>]");
        }

        int servPort = (args.Length == 1) ? Int32.Parse(args[0]) : 11000;

        TcpListener listener = null;

        try
        {
            listener = new TcpListener(IPAddress.Any, servPort);
            listener.Start();

        }
        catch (SocketException se)
        {
            Console.WriteLine(se.ErrorCode + " : " + se.Message);
            Environment.Exit(se.ErrorCode);
        }

        byte[] rcvBuffer = new byte[BUFFSIZE];
        int bytesRcvd;

        for (; ; ) // Loopt altijd
        {
            TcpClient client = null;
            NetworkStream netStream = null;

            try
            {
                client = listener.AcceptTcpClient();
                netStream = client.GetStream();

                Console.Write("Handling client - ");

                int totalBytesEchoed = 0;

                while ((bytesRcvd = netStream.Read(rcvBuffer, 0, rcvBuffer.Length)) > 0)
                {
                    netStream.Write(rcvBuffer, 0, bytesRcvd);
                    totalBytesEchoed += bytesRcvd;
                }

                Console.WriteLine("Echoed {0} bytes.", totalBytesEchoed);

                //Sluiten van de stream en de socket
                netStream.Close();
                client.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                netStream.Close();
            }
        }
    }
}