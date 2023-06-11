using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneChange : MonoBehaviour
{
    public string sceneChangeName;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void SceneChangeActivate(string sceneOverride)
    {
        if( sceneOverride != "")
        {
            SceneManager.LoadScene(sceneOverride, LoadSceneMode.Single );
        }
        else
        {
            SceneManager.LoadScene( sceneChangeName, LoadSceneMode.Single );
        }
    }
    public void quitGame()
    {
        Application.Quit();
        Debug.Log("Quit");
    }
}
