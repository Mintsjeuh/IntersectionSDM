using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class TrafficLigthController : MonoBehaviour
{


    [SerializeField] GameObject[] _trafficLights;

    // Start is called before the first frame update
    void Start()
    {
        //Het ophalen van de verkeerlichten op basis van de tag
        _trafficLights = GameObject.FindGameObjectsWithTag("Trafficlight");
    }

    // Update is called once per frame
    void Update()
    {

    }

    GameObject[] GetTrafficLigths()
    {
        _trafficLights = GameObject.FindGameObjectsWithTag("Trafficligth");

        return _trafficLights;
    }

    void SetTrafficLigths(GameObject[] arrayOfLigths)
    {
        //
    }
}
