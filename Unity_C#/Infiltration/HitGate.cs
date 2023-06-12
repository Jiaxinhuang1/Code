using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HitGate : MonoBehaviour
{
    public GameObject noKeyText;
    public AudioSource gateSound;

    void OnCollisionEnter(Collision other)
    {
        if(other.collider.tag == "Team2")
        {
            if (ScoringSystem.theKey >= 1)
            {
                GetComponent<Animator>().SetTrigger("open");
                ScoringSystem.theKey -= 1;
                gateSound.Play();

            }
            
        }

    }
    private void OnCollisionStay(Collision collision)
    {
        if(collision.collider.tag =="Team2")
        {
            noKeyText.SetActive(true);
        }
    }
    private void OnCollisionExit(Collision collision)
    {
        if(collision.collider.tag =="Team2")
        {
            noKeyText.SetActive(false);
        }
    }
}
