using System;                   // voor String en Console
using System.Net;               // voor DNS, IPHostEntry, IPAddress
using System.Net.Sockets;       //For SocketException
class IPAddresExample
{
    public static void PrintHostInfo(string host)
    {
        try
        {
            IPHostEntry hostInfo;

            hostInfo = Dns.GetHostEntry(host);

            // Toont de hoofd hostname
            Console.WriteLine("\t Canonical Name: " + hostInfo.HostName);

            //Toont een lijst van ip-adressen voor de host
            Console.Write("\tIP Adressses:  ");
            foreach (IPAddress ipaddr in hostInfo.AddressList)
            {
                Console.Write(ipaddr.ToString() + " ");
            }
            Console.WriteLine();

            // Toont lijst met aliassen van de host
            Console.Write("\t Aliases:  ");
            foreach (String alias in hostInfo.Aliases)
            {
                Console.Write(alias + " ");
            }
            Console.WriteLine("\n");

        }
        catch (Exception)
        {
            Console.WriteLine("\tUnable to resolve host: " + host + "\n");
        }
    }
}