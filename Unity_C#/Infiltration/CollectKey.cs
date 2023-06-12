using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollectKey : MonoBehaviour
{
    public AudioSource keySound;
    public GameObject gun;

    private void OnTriggerEnter(Collider other)
    {
        keySound.Play();
        ScoringSystem.theKey += 1;
        Destroy(gameObject);
        Instantiate(Resources.Load("collectcoin"), gun.transform.position, gun.transform.rotation);
    }
}
