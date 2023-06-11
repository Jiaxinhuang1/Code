using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.EventSystems;

public class SceneChange : MonoBehaviour
{
    // Start is called before the first frame update

    public void ChangeScene(string Scene)
    {
        // Debug.Log("BUTTON IS BEING PRESSED");

        // put EXACT name of scene in public variable in --
        //Onclick, drag this script, open this function, put target screen name
        SceneManager.LoadScene(Scene, LoadSceneMode.Single);
    }
}
