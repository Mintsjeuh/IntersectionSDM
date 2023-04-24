using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using lightNamespace;
using System;

public class TrafficLightScript : MonoBehaviour
{
    public SpriteRenderer mySpriteRenderer;
    public double lightId;
    public TrafficLightStatus status;

    // For testing
    private float _timer = 0;
    private float _timeUntilChange = 4;

    // Update is called once per frame
    void Update()
    {
        if (_timer < _timeUntilChange)
        {
            _timer = _timer + Time.deltaTime;
        }
        else
        {
            ChangeTrafficLightColor();
            _timer = 0;
        }
    }

    public TrafficLightStatus ChangeTrafficLightColor()
    {
        // For testing: generates a random color and changes the sprite color to that color
        Array values = Enum.GetValues(typeof(TrafficLightStatus));
        System.Random random = new System.Random();
        TrafficLightStatus randomStatus = (TrafficLightStatus)values.GetValue(random.Next(values.Length));

        if (randomStatus == TrafficLightStatus.Red)
        {
            mySpriteRenderer.color = Color.red;
        }

        if (randomStatus == TrafficLightStatus.Orange)
        {
            mySpriteRenderer.color = new Color(255, 165, 0);
        }

        if (randomStatus == TrafficLightStatus.Green)
        {
            mySpriteRenderer.color = Color.green;
        }

        return randomStatus;
    }
}
