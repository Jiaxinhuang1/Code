using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PowerUps : MonoBehaviour
{
    private Rigidbody2D playerBody;
    public float jumpForce;
    Vector2 direction;
    public float speed;
    private float speedTimer;
    public PlayerMovement moveSpeed;
    private bool isSpeeding;
    public AudioClip[] clipsSound;
    private AudioSource aS;


    // made a seperate script bc the other was just getting too messy ugh 

    // Start is called before the first frame update
    void Start()
    {
        playerBody = GetComponent<Rigidbody2D>();
        PlayerMovement moveSpeed = this.GetComponent<PlayerMovement>();
        PlayerMovement.moveSpeed = 8;
        speedTimer = 0;
        aS = GetComponent<AudioSource>();

    }

    private void Update()
    {
        if (isSpeeding)
        {
            speedTimer += Time.deltaTime;
            Invoke("turnOff", 3f);
        }
    }

    private void turnOff()
    {
        isSpeeding = false;
        Debug.Log("It's been 3 seconds stop tf");
        speedTimer = 0;
        PlayerMovement.moveSpeed = 8;
        isSpeeding = false;
    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.tag == "JumpUp")
        {
            direction = transform.TransformDirection(Vector3.up * jumpForce);
            playerBody.AddForce(direction, ForceMode2D.Impulse);
            PlaySoundEffect(0);

        }
        Destroy(collision.gameObject);

        // doubles speed but it doesn't stop aaaaaa
        if (collision.tag == "SpeedBoost")
        {

            isSpeeding = true;
            if (isSpeeding == true)
            {
                
                
                PlayerMovement.moveSpeed = 14;
                Debug.Log("WE ARE ZOOMING");
                PlaySoundEffect(0);

            }
            Destroy(collision.gameObject);
        }
    }

    public void PlaySoundEffect(int index)
    {
        aS.PlayOneShot(clipsSound[index]);
    }
}
