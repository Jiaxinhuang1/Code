using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Item : MonoBehaviour
{
    public GameManager.ItemType itemType;
    private bool isClicked;

    // Start is called before the first frame update
    void Start()
    {
        isClicked = false;
        LeanTween.moveY(gameObject, transform.position.y + Random.Range(-1f, 1f), Random.Range(1f, 3f)).setEase(LeanTweenType.easeInOutCubic).setLoopPingPong();
        //LeanTween.moveX(gameObject, transform.position.x + Random.Range(0.01f, 1f), Random.Range(1f, 3f)).setEase(LeanTweenType.easeInOutCubic).setLoopPingPong();
        LeanTween.rotateZ(gameObject, Random.Range(-10, 10), 1f).setEaseInCubic().setLoopPingPong();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void ClickItem()
    {
        //Debug.Log("Clicked");
        if (!isClicked)
        {
            if (GameManager.instance.itemType == itemType)
            {
                GameManager.instance.CollectItem();
                LeanTween.scale(gameObject, new Vector3(0, 0, 0), 0.3f).setDestroyOnComplete(true);
                Instantiate(Resources.Load("Collect"), transform.position, transform.rotation);
            }
            else
            {
                GameManager.instance.ShakeCamera(0.1f, 0.1f);
                GameManager.instance.IncreaseErrorCount();
                LeanTween.scale(gameObject, new Vector3(0, 0, 0), 0.3f).setDestroyOnComplete(true);
                GameObject explosion = Instantiate(Resources.Load("Explosion"), this.gameObject.transform.position, transform.rotation) as GameObject;
                Destroy(explosion, 0.5f);

            }
            isClicked = true;
        }
    }

    public void ResetClick()
    {
        isClicked = false;
        Debug.Log("PointerUp");
    }


}
