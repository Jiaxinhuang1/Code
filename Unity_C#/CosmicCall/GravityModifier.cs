using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GravityModifier : MonoBehaviour
{
    private bool changeGravity;
    private bool notified = false;

    private void Start()
    {
        changeGravity = false;
    }

    private void Update()
    {
        // when gravity is changed, the new gravity down is less than the normal acceleration in earth
        if(changeGravity)
        {
            Physics.gravity = new Vector3(0, -4f, 0);
        }
        //when gravity back to default, the gravity is changed back to normal acceleration on earth
        else
        {
            Physics.gravity = new Vector3(0, -9.81f, 0);
        }
    }

    // when player enters gravity zone, gravity is changed from default
    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Robot" | other.tag == "Alien")
        {
            changeGravity = true;
            // print once when enter the zone
            if (!notified)
            {
                Debug.Log("Entered Gravity Zone");
                notified = true;
            }
        }
    }
    // when player exits gravity zone, gravity is changed back to default
    private void OnTriggerExit(Collider other)
    {
        if (other.tag == "Robot" || other.tag == "Alien")
        {
            changeGravity = false;
            // print once when exit the zone
            Debug.Log("Exited Gravity Zone");
            notified = false;
        }
    }

}
