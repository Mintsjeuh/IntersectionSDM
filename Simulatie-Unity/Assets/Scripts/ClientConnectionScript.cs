using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using sleep = System.Threading.Thread;

public class ClientConnectionScript : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        TcpConnection();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public static void TcpConnection()
    {
        try
        {
            TcpClient client = new TcpClient();
            Debug.Log("\n Connecting...");
            // 127.0.0.1 -> local host
            //
            client.Connect("", 11000);

            Debug.Log("Connected");
            while (client.Connected)
            {
                Stream stream = client.GetStream();
                UTF8Encoding encoding = new UTF8Encoding();

                // The data that will be send
                double busDouble = 42.0;
                string testString = "[{" + '"' + "id" + '"' + ':' + busDouble + ',' + '"' + "weight" + '"' + ':' + 1 + "}]";

                // Sends data to the server
                byte[] sendData = Encoding.UTF8.GetBytes(testString);
                Debug.Log("Sending data to server");
                stream.Write(sendData, 0, sendData.Length);

                // Receives data from the server
                byte[] receiveBytes = new byte[1024];
                int receiveData = stream.Read(receiveBytes, 0, receiveBytes.Length);
                string result = Encoding.UTF8.GetString(receiveBytes);
                Debug.Log("Result: " + result);

                // Clears the stream a.k.a. flushes the stream
                stream.Flush();
                sleep.Sleep(2000);
            }
            client.Close();
        }
        catch (Exception e)
        {
            Debug.LogException(e);
        }
    }
}
