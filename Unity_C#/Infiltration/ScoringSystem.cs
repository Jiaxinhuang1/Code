using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;


public class ScoringSystem : MonoBehaviour
{
    public GameObject healthText;
    public static int theHealth = 50;
    public static int theKey = 0;
    public GameObject keyText;


    private void Update()
    {
        healthText.GetComponent<Text>().text = "HEALTH: " + theHealth;
        keyText.GetComponent<Text>().text = "KEY: " + theKey;
        if (theHealth <= 0)
        {
            Scene scene = SceneManager.GetActiveScene(); SceneManager.LoadScene(scene.name);
            theHealth = 50;
        }
      
    }
}
