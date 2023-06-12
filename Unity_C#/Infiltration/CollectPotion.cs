using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollectPotion : MonoBehaviour
{
    public AudioSource collectSound;
    public GameObject gun;
    private void OnTriggerEnter(Collider other)
    {
        collectSound.Play();
        ScoringSystem.theHealth += 5;
        Destroy(gameObject);
        Instantiate(Resources.Load("potion"), gun.transform.position, gun.transform.rotation);
    }
}
