using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[Serializable]
public class TrafficLigth : MonoBehaviour
{

    public SpriteRenderer LigthSprite;
    public Sprite[] spriteArray = new Sprite[10];
    [SerializeField]
    public double Id { get; set; }
    [SerializeField]
    public int Status { get; set; }

    LigthStatus status = LigthStatus.Red;


    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        switch (status)
        {
            default:
                LigthSprite.sprite = spriteArray[0];
                Debug.Log("Red");
                break;
            case LigthStatus.Orange:
                LigthSprite.sprite = spriteArray[1];
                Debug.Log("Orange");
                break;
            case LigthStatus.Green:
                LigthSprite.sprite = spriteArray[2];
                Debug.Log("Green");
                break;
        }
    }
}


enum LigthStatus
{
    Red = 0,
    Orange = 1,
    Green = 2
}


