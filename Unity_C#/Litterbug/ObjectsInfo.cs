using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class ObjectsInfo : MonoBehaviour
{
    private int itemCost;
    private string itemCostString;
    public ShopManager shopManager;
    public UIManager uiManager;
    

    public int recycleBoost = 0;

    // Start is called before the first frame update
    void Start()
    {
        // Get the information in the text field of the children of this gameobject
        itemCostString = this.gameObject.GetComponentInChildren<Text>().text;
        // Convert the text string into int
        int.TryParse(itemCostString, out itemCost);
        //Debug.Log(this.gameObject.name + itemCost);
    }

    // Update is called once per frame
    void Update()
    {
        // If the player's Ecocoins is greater than or equal to the cost, the buy button is interactable
        if (shopManager.ecoCoins >= itemCost)
        {
            this.gameObject.GetComponent<Button>().interactable = true;
        }
        // If the player does not have enough EcoCoins, the buy button is disabled. 
        else
        {
            this.gameObject.GetComponent<Button>().interactable = false;
        }
    }

    public void itemBought()
    {
        shopManager.ecoCoins -= itemCost;
        this.gameObject.SetActive(false);
    }

    public void BuyRecycleBoost()
    {
        itemCostString = this.gameObject.GetComponentInChildren<Text>().text;
        int.TryParse(itemCostString, out itemCost);
        if (recycleBoost != 100)
        {
            shopManager.ecoCoins -= itemCost;
            this.gameObject.GetComponentInChildren<Text>().text = (itemCost + 30).ToString();
            recycleBoost += 20;
        }
        else
        {
            this.gameObject.SetActive(false);
        }
    }

    public void BuyEarlyGarbage()
    {
        itemCostString = this.gameObject.GetComponentInChildren<Text>().text;
        int.TryParse(itemCostString, out itemCost);
        if (uiManager.timeLeftVal != 85)
        {
            shopManager.ecoCoins -= itemCost;
            this.gameObject.GetComponentInChildren<Text>().text = (itemCost + 20).ToString();
            uiManager.timeLeftVal -= 3;
            uiManager.timeSlider.maxValue = uiManager.timeLeftVal;
        }
        else
        {
            this.gameObject.SetActive(false);
        }
    }

    public void coolDownFinished()
    {
        this.gameObject.SetActive(true);
    }

    public void RemoveElement(ref GameObject[] array, int index)
    {
        for (int i = index; i < array.Length - 1; i++)
        {
            array[i] = array[i + 1];
        }
        Array.Resize(ref array, array.Length - 1);
    }
}
