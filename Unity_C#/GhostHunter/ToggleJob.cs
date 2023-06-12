using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ToggleJob : MonoBehaviour
{
    // This script is attached to each job toggle which checks to see if it is on and save it to player prefs
    private Toggle toggle;
    public GameObject weapon;
    public int weaponIndex;
    public CharCusSave charCusSave;

    // Start is called before the first frame update
    void Start()
    {
        toggle = this.GetComponent<Toggle>();
    }

    // Update is called once per frame
    void Update()
    {
        // when toggle is on, display the weapon gameobject (can change depending on which is attached to inspector)
        // and add the weapon index (can change depending on which is set in inspector) to player prefs
        if (toggle.isOn)
        {
            weapon.SetActive(true);
            if (charCusSave.isSlotOne)
            {
                PlayerPrefs.SetInt("OneWeapon", weaponIndex);
            }
            else if (charCusSave.isSlotTwo)
            {
                PlayerPrefs.SetInt("TwoWeapon", weaponIndex);
            }
            else if (charCusSave.isSlotThree)
            {
                PlayerPrefs.SetInt("ThreeWeapon", weaponIndex);
            }
        }
        else if (!toggle.isOn)
        {
            weapon.SetActive(false);
        }

    }
}
