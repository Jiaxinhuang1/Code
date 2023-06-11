using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoilingArea : MonoBehaviour
{
    private int timeCount = 5;
    private bool takingAway = false;
    private int health = 100;
    private bool canBoil = true;
    private int timeBetweenBoils = 2;

    private bool isBoiling = false;
    private bool notified = false;


    void Update()
    {
        // count down time before health starts decreasing when there is still time and player inside boiling zone
        if (!takingAway && isBoiling && timeCount > 0)
        {
            StartCoroutine(CountDown());
        }
    }

    // when the player stays inside boiling zone
    private void OnTriggerStay(Collider other)
    {
        if (other.tag == "Robot" || other.tag == "Alien")
        {
            isBoiling = true;
            // print message once
            if (!notified)
            {
                Debug.Log("Entered Boiling Zone");
                notified = true;
            }
            // when time count is 0 (stay too long in zone) decrease health by 5 every 2 seconds
            if (timeCount == 0 && canBoil && isBoiling)
            {
                health -= 5;
                canBoil = false;
                Debug.Log("Health: " + health);
                Invoke(nameof(ResetAttack), timeBetweenBoils);
            }
        }
    }

    // when player exit boiling zone, time count is back and print
    private void OnTriggerExit(Collider other)
    {
        if (other.tag == "Robot" || other.tag == "Alien")
        {
            isBoiling = false;
            timeCount = 5;
            Debug.Log("Exited Boiling Zone");
            notified = false;
        }
    }
    
    // resets attack so it can be invoked to take damage every 2 seconds
    private void ResetAttack()
    {
        canBoil = true;
    }

    // countdown the time before damage is taken
    IEnumerator CountDown()
    {
        takingAway = true;
        yield return new WaitForSeconds(1);
        timeCount -= 1;
        Debug.Log("CountDown: " + timeCount);
        takingAway = false;
    }
}
