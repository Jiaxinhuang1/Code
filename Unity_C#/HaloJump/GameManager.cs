using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{

    public AudioClip[] clipsMusic;
    private AudioSource aS;

    // Start is called before the first frame update
    void Start()
    {
        if (FindObjectsOfType<GameManager>().Length > 1)
        {
            Destroy(this.gameObject);
        }
        else
        {
            DontDestroyOnLoad(this.gameObject);
        }
        aS = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {
        if (SceneManager.GetActiveScene().buildIndex == 0 || SceneManager.GetActiveScene().buildIndex == 1)
        {
            if (aS.clip != clipsMusic[0] || !aS.isPlaying)
            {
                aS.clip = clipsMusic[0];
                aS.Play();
            }
        }
        if (SceneManager.GetActiveScene().buildIndex == 2)
        {
            if (aS.clip != clipsMusic[1] || !aS.isPlaying)
            {
                aS.clip = clipsMusic[1];
                aS.Play();
            }
        }
    }

}
