using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;


public class Triggers : MonoBehaviour
{
    private int keyCount = 0;
    private int healthCount = 10;
    public Text Health;
    public Text Key;

    private void OnTriggerEnter(Collider other)
    {
            if (other.gameObject.tag =="key")
        {
            Destroy(other.gameObject);
            keyCount = keyCount + 1;
            Key.text = "KEY: " + keyCount;
            if (keyCount >= 1)
            {
                if (other.gameObject.tag =="gate")
                {
                    Destroy(other.gameObject);
                    keyCount = keyCount - 1;
                }
            }
            if (other.gameObject.tag == "potion")
            {
                Destroy(other.gameObject);
                Debug.Log("asasd");
                healthCount = healthCount + 1;
                Health.text = "HEALTH: " + healthCount;
            }
            if (other.gameObject.tag == "trap")
            {
                Debug.Log("asdasd");
                healthCount = healthCount - 2;
            }
            if (healthCount <= 0)
            {
                SceneManager.LoadScene("newdemo");
            }
        }
    }

}
