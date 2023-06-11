using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class enemyHealth : MonoBehaviour
{
    public Slider enemyBar;
    private int goblinHealth;

    public GameObject impactParticle;
    public GameObject hitParticle;
    public Vector3 impactNormal;

    public AudioSource explodeSound;
    public AudioSource hitSound;

    public GameObject goblin;
    Animator anim;

    private BoxCollider collider;
    // Start is called before the first frame update
    void Start()
    {
        collider = this.GetComponent<BoxCollider>();
        goblinHealth = 100;
        anim = this.GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        enemyBar.value = goblinHealth;
    }
    public void OnCollisionEnter(Collision collision)
    {
        if (collision.collider.tag == "bullet")
        {
            goblinHealth -= 10;
            hitParticle = Instantiate(hitParticle, transform.position, transform.rotation) as GameObject;          
            //Destroy(hitParticle, 3);
            Instantiate(hitSound);
            Destroy(collision.gameObject);
            //explodeSound.GetComponent<AudioSource>().Play();
            if (goblinHealth <= 0)
            {
                //EnemyRespawn.Death = true;
                Instantiate(explodeSound);
                //Destroy(gameObject);
                collider.isTrigger = true;
                anim.SetBool("Death", true);
                gameObject.tag = "death";
                impactParticle = Instantiate(impactParticle, transform.position, Quaternion.FromToRotation(Vector3.up, impactNormal)) as GameObject;
                Destroy(impactParticle, 3);
                Destroy(collision.gameObject);
            }

        }
    }
}
