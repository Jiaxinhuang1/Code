using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextActive : MonoBehaviour
{
    public ObjectsInfo objectsInfo;
    public GameObject maxText;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (objectsInfo.recycleBoost == 100)
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
