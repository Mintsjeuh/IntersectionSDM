using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
//using System.Text.Json;
//using System.Text.Json.Serialization;
using UnityEditor.PackageManager;
using UnityEngine;
using sleep = System.Threading.Thread;



public class ConnectionScript : MonoBehaviour
{

    GameObject[] TrafficLigths;


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
            //client.Connect("141.252.225.247", 11000);
            // 127.0.0.1 -> local host
            client.Connect("141.252.225.58", 11000);

            Debug.Log("Connected");
            while (true)
            {

                Stream stream = client.GetStream();
                UTF8Encoding encoding = new UTF8Encoding();

                //Ophalen van de data uit de simulator
                //TrafficLigths = GameObject.FindGameObjectsWithTag("Trafficligth");



                // DATA DAT WORDT VERZONDEN
                double busDouble = 42.0;
                string testString = "[{" + '"' + "id" + '"' + ':' + busDouble + ',' + '"' + "weight" + '"' + ':' + 1 + "}]";


                //Weight zetten in een dictionary


                //Dictionary omzetten in json (serialiseren)






                //Encoden naar UTF-8 voor versturen




                //Versturen naar de server
                byte[] sendData = Encoding.UTF8.GetBytes(testString);
                Debug.Log("Transmitting data");
                stream.Write(sendData, 0, sendData.Length);




                //Ontvangen van de server
                byte[] receiveBytes = new byte[1024];
                int receiveData = stream.Read(receiveBytes, 0, receiveBytes.Length);

                // decode naar UTF-8
                string result = Encoding.UTF8.GetString(receiveBytes);
                Debug.Log(result);



                // Omzetten naar JSON string (Deseraliseren)



                //String omzetten naar een dictionary met id en status


                //Status van  trafficligths zetten met id.



                // Clears the stream a.k.a. flushes the stream
                stream.Flush();
                sleep.Sleep(2000);
            }
        }
        catch (Exception e)
        {
            Debug.LogException(e);
        }
    }


    public void GetDataFromSimulator()
    {

    }

    public void SetTrafficLigths()
    {

    }

}



//[Serializable]
//public class IncommingMessage
//{
//    public double Id { get; set; }
//    public int Status { get; set; }
//}

//[Serializable]
//public class OutgoingMessage
//{
//    public double Id { get; set; }
//    public int weigth { get; set; }
//}
