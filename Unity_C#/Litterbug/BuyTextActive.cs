using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BuyTextActive : MonoBehaviour
{
    public UIManager uiManager;
    public GameObject maxText;
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (uiManager.timeLeftVal == 85)
        {
            maxText.SetActive(true);
            this.gameObject.SetActive(false);
        }
        else
        {
            maxText.SetActive(false);
            this.gameObject.SetActive(true);
        }
    }
}
