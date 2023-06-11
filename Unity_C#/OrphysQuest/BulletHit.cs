using System.Collections;
using System.Collections.Generic;
using UnityEngine;
//using UnityEngine.UI;

public class BulletHit : MonoBehaviour
{
    public GameObject impactParticle;
    public Vector3 impactNormal;
    public GameObject apple;

    public AudioSource explodeSound;



    GameObject appleTree;

    //public Slider enemyBar;
    //public int enemyHealth;

    //public AudioSource explodeSound;
    //public Animator anim;
    // Start is called before the first frame update
    void Start()
    {
        appleTree = GameObject.FindWithTag("appleFallArea");
        //enemyHealth = 100;
    }

    // Update is called once per frame
    void Update()
    {
        //enemyBar.value = enemyHealth;
    }
    public void OnCollisionEnter(Collision collision)
    {
        /*if(collision.collider.tag == "enemy")
        {
            enemyHealth -= 10;
            //explodeSound.GetComponent<AudioSource>().Play();
            if (enemyHealth <= 0)
            {
                EnemyRespawn.Death = true;
                Instantiate(explodeSound);
                Destroy(gameObject);
                impactParticle = Instantiate(impactParticle, transform.position, Quaternion.FromToRotation(Vector3.up, impactNormal)) as GameObject;
                Destroy(impactParticle, 3);
                Destroy(collision.gameObject);
                if (DialogueQuest.killQuestActive == true || DialogueQuest.killQuestCompleted == true)
                {
                    DetectCollision.killedCount += 1;
                }
            }

        }*/
        if(collision.collider.tag == "appleTree")
        {
            
            Instantiate(apple, appleTree.transform.position *Random.Range(1.01f,1.05f), appleTree.transform.rotation);
        }

        if(collision.collider.tag=="terrain")
        {
            Destroy(gameObject);
        }
    }
}
