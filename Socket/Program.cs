using System.Net.Sockets;
using System.Net;

using System;

namespace HelloServer
{
    class Program
    {


        static void Main(string[] args)
        {
            TcpClient.Main();
        }

        // static void Main(string[] args)
        // {

        //     try
        //     {
        //         Console.WriteLine("Local Host:");
        //         String localHostName = Dns.GetHostName();
        //         Console.WriteLine("\t Host Name: " + localHostName);

        //         IPAddresExample.PrintHostInfo(localHostName);
        //     }
        //     catch (Exception)
        //     {

        //         Console.WriteLine("Unable to get local host\n");
        //     }

        //     foreach (String arg in args)
        //     {
        //         Console.WriteLine(arg + ":");
        //         IPAddresExample.PrintHostInfo(arg);
        //     }
        // }
    }
}