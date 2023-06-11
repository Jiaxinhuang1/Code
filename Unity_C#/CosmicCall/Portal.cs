using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Portal : MonoBehaviour
{
    public Transform spawnArea;
    [SerializeField] private bool canEnter = true;
    private float refreshTime = 2f;

    // function to reset bool to make player enter
    private void ResetTime()
    {
        canEnter = true;
    }
    
    void OnTriggerEnter(Collider other)
    {
        // if the player enters the object with this script, move player to spawnAre
        if ((other.gameObject.tag == "Robot" || other.gameObject.tag == "Alien") && canEnter)
        {
            // with position offset to prevent infinite loop
            other.gameObject.transform.position = new Vector3(spawnArea.position.x * 1.2f, spawnArea.position.y, spawnArea.position.z);
            canEnter = false;   //set canEnter to false so cannot enter right away
            // resets canEnter to true after 2 sec
            Invoke(nameof(ResetTime), refreshTime);
        }
    }

}
