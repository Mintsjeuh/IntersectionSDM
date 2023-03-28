using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CarSpawnerScript : MonoBehaviour
{
    public GameObject Car;
    public float spawnRate = 7;
    private float timer = 0;

    // Start is called before the first frame update
    void Start()
    {
        SpawnCar();
    }

    // Update is called once per frame
    void Update()
    {
        if (timer < spawnRate)
        {
            timer = timer + Time.deltaTime;
        }
        else
        {
            SpawnCar();
            timer = 0;
        }
    }

    void SpawnCar()
    {
        // Puts the car on the position of the gameObject
        Instantiate(Car,transform.position, transform.rotation);
    }
}
