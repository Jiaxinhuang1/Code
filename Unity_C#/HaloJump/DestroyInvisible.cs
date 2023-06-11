using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyInvisible : MonoBehaviour
{
    private float secondsToDestroy = 40f;
    private GameObject Player;
    void Start()
    {
        Player = GameObject.FindGameObjectWithTag("Player");
    }
    private void Update()
    {
        if (Vector3.Distance(transform.position, Player.transform.position) > 300f)
        {
            Destroy(gameObject);
        }
    }

}
