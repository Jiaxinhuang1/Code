using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class destroyTime : MonoBehaviour
{
    public float timeLeft = 3.0f;

    void Update()
    {
        timeLeft -= Time.deltaTime;
        if(timeLeft<0)
        {
            Destroy(gameObject);
        }

    }

}
