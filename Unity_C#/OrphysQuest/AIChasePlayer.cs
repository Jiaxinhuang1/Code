using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class AIChasePlayer : MonoBehaviour
{
    GameObject player;
    Animator anim;
    public AudioSource hitSound;
    //public AudioSource explodeSound;
    private NavMeshAgent agent;
    //public GameObject goblin;


    // Start is called before the first frame update
    void Start()
    {
        player = GameObject.FindWithTag("Player");
        agent = this.GetComponent<NavMeshAgent>();
        anim = this.GetComponent<Animator>();
        anim.SetBool("Idle", true);
        anim.SetBool("RUN", false);

    }

    // Update is called once per frame
    void Update()
    {
        if (Vector3.Distance(player.transform.position, transform.position) > 25)
        {
            anim.SetBool("Attack", false);
            anim.SetBool("RUN", false);
            anim.SetBool("Idle", true);
            agent.SetDestination(transform.position);
        }
        else if (Vector3.Distance(player.transform.position, transform.position) <= 25)
        {
            anim.SetBool("Attack", false);
            anim.SetBool("Idle", false);
            anim.SetBool("RUN", true);
            agent.SetDestination(player.transform.position);
            if (Vector3.Distance(player.transform.position, transform.position) <= 2)
            {
                anim.SetBool("RUN", false);
                anim.SetBool("Attack", true);
                //hitSound.Play();
            }
        }
        if(gameObject.tag == "death")
        {
            agent.SetDestination(transform.position);
        }
    }   


    /*public void OnCollisionEnter(Collision collision)
    {
        if (collision.collider.tag == "Player")
        {
            Debug.Log("stay");
            anim.SetBool("RUN", false);
            anim.SetBool("Attack", true);
        }
    }
    public void OnCollisionExit(Collision collision)
    {
        if (collision.collider.tag == "Player")
        {
            Debug.Log("exit");
            anim.SetBool("RUN", true);
            anim.SetBool("Attack", false);

        }
    }*/

    void GetDamage()
    {
        DetectCollision.healthCount -= 10;
        Instantiate(hitSound);
        Instantiate(Resources.Load("hurt"), transform.position, transform.rotation);

    }

}
