using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TrafficLightScript : MonoBehaviour
{
    public SpriteRenderer mySpriteRenderer;
    enum TrafficLightStatus{
        Red,
        Orange,
        Green
    }

    // default state of red
    TrafficLightStatus status = TrafficLightStatus.Red;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        switch (status)
        {
            case TrafficLightStatus.Red:
                mySpriteRenderer.color = Color.red;
                break;
            case TrafficLightStatus.Orange:
                mySpriteRenderer.color = new Color(255, 165, 0);
                break;
            case TrafficLightStatus.Green: 
                mySpriteRenderer.color = Color.green; 
                break;
        }
    }
}
