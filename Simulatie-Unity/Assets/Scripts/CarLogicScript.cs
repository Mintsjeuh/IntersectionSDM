using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CarLogicScript : MonoBehaviour
{
    [SerializeField]
    float moveSpeed = 2f;

    int waypointIndex = 0;

    public Rigidbody2D myRigidbody;
    private Transform[] _waypoints;

    float deadzoneLeftSide = -25;
    float deadzoneRightSide = 32;
    float deadzoneTopSide = 10;
    float deadzoneBottomSide = -11;

    // Update is called once per frame
    void Update()
    {
        if (_waypoints.Length != 0)
        {
            Move(_waypoints);
        }

        if (transform.position.x < deadzoneLeftSide)
        {
            Destroy(gameObject);
        }
        if (transform.position.x > deadzoneRightSide)
        {
            Destroy(gameObject);
        }
        if (transform.position.y > deadzoneTopSide)
        {
            Destroy(gameObject);
        }
        if (transform.position.y < deadzoneBottomSide)
        {
            Destroy(gameObject);
        }
    }

    public void Move(Transform[] waypoints)
    {
        transform.position = Vector2.MoveTowards(transform.position, waypoints[waypointIndex].transform.position, moveSpeed * Time.deltaTime);

        if (transform.position == waypoints[waypointIndex].transform.position)
        {
            waypointIndex += 1;
        }
    }

    public void SetWaypoints(Transform[] waypoints)
    {
        _waypoints = waypoints;
    }
}
