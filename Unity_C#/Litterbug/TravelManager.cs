using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class TravelManager : MonoBehaviour
{
    public ShopManager shopManager;
    public GameObject parisButton;
    public GameObject mexicoButton;
    public GameObject austinButton;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (shopManager.travelAustin)
        {
            austinButton.SetActive(true);
        }
        else
        {
            austinButton.SetActive(false);
        }
        if (shopManager.travelParis)
        {
            parisButton.SetActive(true);
        }
        else
        {
            parisButton.SetActive(false);
        }
        if (shopManager.travelMexico)
        {
            mexicoButton.SetActive(true);
        }
        else
        {
            mexicoButton.SetActive(false);
        }

    }
    public void travelToParis()
    {
        SceneManager.LoadScene("Paris");
    }
    public void travelToAustin()
    {
        SceneManager.LoadScene("Austin");
    }
    public void travelToMexico()
    {
        SceneManager.LoadScene("Mexico");
    }
}
