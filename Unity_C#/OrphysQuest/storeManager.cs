using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class storeManager : MonoBehaviour
{
    public GameObject storePanel;
    private bool isStoreOpen;
    public int breadAmt;
    public int portalAmt;
    public Text noMoneyText;
    public Text breadAmtText;
    public Text portalAmtText;

    public AudioSource buySound;

    public AudioSource eatSound;

    public GameObject portal;

    

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(isStoreOpen)
        {
            storePanel.SetActive(true);
            if (DetectCollision.moneyCount >=20 && Input.GetKeyDown("b"))
            {
                breadAmt += 1;
                DetectCollision.moneyCount -= 20;
                Instantiate(buySound);
            }
            if (DetectCollision.moneyCount >= 50 && Input.GetKeyDown("p"))
            {
                portalAmt += 1;
                DetectCollision.moneyCount -= 50;
                Instantiate(buySound);
            }
            if (DetectCollision.moneyCount < 20)
            {
                noMoneyText.text = "You do not have enough money";
            }
        }
        else
        {
            storePanel.SetActive(false);
            noMoneyText.text = "";
        }
        breadAmtText.text = "x " + breadAmt;
        portalAmtText.text = "x " + portalAmt;
        if (Input.GetKeyDown("1") && breadAmt >= 1)
        {
            Instantiate(eatSound);
            DetectCollision.healthCount += 10;
            breadAmt -= 1;
        }
        if (Input.GetKeyDown("2") && portalAmt >= 1)
        {
            Instantiate(portal, transform.position + (transform.forward * 3), transform.rotation);
            portalAmt -= 1;
        }
    }
    private void OnTriggerEnter(Collider other)
    {
        if(other.gameObject.tag == "storeNPC")
        {
            isStoreOpen = true;
        }

    }
    private void OnTriggerExit(Collider other)
    {
        if(other.gameObject.tag == "storeNPC")
        {
            isStoreOpen = false;
        }
        
    }
}
