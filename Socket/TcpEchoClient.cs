//DIT STAAT OP DE ANDERE COMPUTER IN VS CODE

using System;                   //voor Sting, Int32, Console, ArgumentException
using System.Text;              // voor Encoding
using System.IO;                // voor IOException
using System.Net.Sockets;       // voor TCPClient, NetworkStream, SocketException

namespace HelloClient
{
    class TcpEchoClient
    {
        static void Main(string[] args)
        {
            if ((args.Length < 2) || (args.Length > 3))  // test voor de juiste aantal of args
            {
                throw new ArgumentException("Parameters: <Server> <Word> [<Port>]");
            }


            String server = args[0];        // Server name or IP addres


            //Zet String input om in bytes
            byte[] byteBuffer = Encoding.ASCII.GetBytes(args[1]);

            //Gebruik port argument indien aanwezig, anders gebruikt hij standaard 11000
            int serverPort = (args.Length == 3) ? Int32.Parse(args[2]) : 11000;

            TcpClient client = null;
            NetworkStream netStream = null;


            try
            {   //Creert een socket dat is geconneced is met de server via een specifieke port
                client = new TcpClient(server, serverPort);

                Console.WriteLine("Connected to server... sending echo string");

                netStream = client.GetStream();

                // Stuur de geëncoded string naar de server
                netStream.Write(byteBuffer, 0, byteBuffer.Length);

                Console.WriteLine("Sent {0} bytes to server...", byteBuffer.Length);

                int totalBytesRcvd = 0;
                int bytesRcvd = 0;

                //Ontvang dezelfde string terug vanaf de server
                while (totalBytesRcvd < byteBuffer.Length)
                {
                    if ((bytesRcvd = netStream.Read(byteBuffer, totalBytesRcvd, byteBuffer.Length - totalBytesRcvd)) == 0)
                    {
                        Console.WriteLine("Connection closed prematurely.");
                        break;
                    }
                    totalBytesRcvd += bytesRcvd;
                }
                Console.WriteLine("Received {0} byes from the server: {1}", totalBytesRcvd, Encoding.ASCII.GetString(byteBuffer, 0, totalBytesRcvd));
            }
            catch (Exception e)
            {

                Console.WriteLine(e.Message);
            }
            finally
            {
                netStream.Close();
                client.Close();
            }

        }

    }

}
