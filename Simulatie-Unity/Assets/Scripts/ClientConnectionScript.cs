using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;
using System.Linq;
using UnityEngine.UIElements;

public class ClientConnectionScript
{
    // TODO: singleton
    private List<ISubscriber> subscribers;
    private readonly TcpClient client;
    private readonly Thread thread;

    public ClientConnectionScript(string ipAddress, short portNumber)
    {
        subscribers = new List<ISubscriber>();
        client = new TcpClient(ipAddress, portNumber);
        thread = new Thread(() => Run());
    }

    // Destructor
    ~ClientConnectionScript() =>

        client.Close();

    public bool Write(string message)
    {
        try
        {
            byte[] sendData = Encoding.UTF8.GetBytes($"{message}\n");
            client.GetStream().Write(sendData, 0, sendData.Length);
        }
        catch (Exception e)
        {
            Debug.LogException(e);
            return false;
        }
        return true;
    }

    public void Subscribe(ISubscriber subscriber)
    {
        subscribers.Add(subscriber);
    }

    public void Run()
    {
        while (client.Connected)
        {
            byte[] receivedBytes = new byte[1024];
            NetworkStream stream = client.GetStream();
            byte[] buffer = new byte[1024];
            int length;
            while ((length = stream.Read(buffer, 0, buffer.Length)) != 0)
            {
                var incomingData = new byte[length];
                Array.Copy(buffer, 0, incomingData, 0, length);
                string serverMessage = Encoding.UTF8.GetString(incomingData);

                Debug.Log(serverMessage);
                //Dictionary<double, int> json = JSON.StringToDictionary(serverMessage);
                //SimulationController.Instance.Orders = json;
                // TODO: Convert serverMessage from JSON to TrafficOrder.
                //Debug.Log("server message received as: " + mockjson);


            }


            stream.Read(receivedBytes, 0, receivedBytes.Length);
            string receivedData = Encoding.UTF8.GetString(receivedBytes);

            Debug.Log(receivedData);
            //foreach (string line in receivedData.Split('\n'))
            //{
            //    // TODO: JSON deserialize - received

            //    foreach (ISubscriber subscriber in subscribers)
            //    {
            //        // TODO: Call subscribers
            //    }
            //}
        }
    }

    // All classes can subscribe and will receive their right model
    public interface ISubscriber
    {
        // TODO: Add JSON model parameter
        void OnReceive();
    }
}
