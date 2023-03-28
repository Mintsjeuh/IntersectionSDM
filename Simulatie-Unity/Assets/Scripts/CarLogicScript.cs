using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CarLogicScript : MonoBehaviour
{
    [SerializeField]
    float accelerationPower = 2.5f;
    [SerializeField]
    float steeringPower = 2.5f;
    float steeringAmount, speed, direction;

    public float deadZoneLeft = -25;
    public float deadZoneRight = 25;

    public Rigidbody2D myRigidbody;


    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (transform.position.x < deadZoneLeft)
        {
            Debug.Log("Car left deleted");
            Destroy(gameObject);
        }
        else if (transform.position.x > deadZoneRight)
        {
            Debug.Log("Car right deleted");
            Destroy(gameObject);
        }
    }

    // Frame-rate independent for physics calculations
    void FixedUpdate()
    {
        // Kijkt of de linker of rechter arrowkey is ingedrukt als negatieve waarde
        steeringAmount = - Input.GetAxis("Horizontal");

        // Kijkt of de up of down arrowkey is ingedrukt, vermenigvuldigd met de acceleratie power
        speed = Input.GetAxis("Vertical") * accelerationPower;

        // De richting wordt berekend
        // Vector2.Dot --> returnt een positieve waarde als de vectoren in de zelfde richting wijzen, anders een negatieve waarde
        // Mathf.Sign --> returnt 1 als hij positief of 0 is en -1 als hij negatief is
        direction = Mathf.Sign(Vector2.Dot(myRigidbody.velocity, myRigidbody.GetRelativeVector(Vector2.up)));
        myRigidbody.rotation += steeringAmount * steeringPower * myRigidbody.velocity.magnitude * direction;

        // Beweegt een auto vooruit of achteruit
        myRigidbody.AddRelativeForce(Vector2.right * speed);

        // Beweegt een auto links en rechts
        myRigidbody.AddRelativeForce( - Vector2.right * myRigidbody.velocity.magnitude * steeringAmount / 2);
    }
}
