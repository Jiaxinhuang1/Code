using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HitTrap : MonoBehaviour
{
    public AudioSource trapSound;
    public GameObject gun;

    private void OnTriggerEnter(Collider other)
    {
        trapSound.Play();
        ScoringSystem.theHealth -= 10;
        Instantiate(Resources.Load("traphit"), gun.transform.position, gun.transform.rotation);
    }

}
