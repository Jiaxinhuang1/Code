using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DisableGameObject : MonoBehaviour
{
    public void setInactive()
    {
        this.gameObject.SetActive(false);
    }

    public void checkTutorial()
    {
        if ((PlayerPrefs.GetString("Tutorial")) == "ON")
        {
            this.gameObject.SetActive(true);
        }
        else
        {
            this.gameObject.SetActive(false);
        }
    }
}
