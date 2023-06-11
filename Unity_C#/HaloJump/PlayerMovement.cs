using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public bool start = false;
    private bool jump = false;
    public bool isGrounded;
    public static float moveSpeed;
    public float jumpForce;
    private Rigidbody2D rb;
    public AudioClip[] clipsSound;
    private AudioSource aS;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        aS = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {

        if (start)
        {
            GetComponent<Animator>().SetBool("IsIdling", false);
            GetComponent<Animator>().SetBool("IsRunning", true);
            rb.velocity = new Vector2(moveSpeed, rb.velocity.y);

            //set for double jump
            if (isGrounded)
            {
                jump = true;
            }

            if ((Input.touchCount > 0 || Input.GetKeyDown(KeyCode.Space) || Input.GetMouseButtonDown(0)))
            {
                //Touch touch = Input.GetTouch(0);

                // if player on ground, can jump then double jump
                if (isGrounded)
                {
                    if (SystemInfo.deviceType == DeviceType.Handheld)
                    {
                        Touch touch = Input.GetTouch(0);
                        Debug.Log("Mobile");
                        switch (touch.phase)
                        {
                            case TouchPhase.Began:
                                GetComponent<Animator>().SetBool("IsRunning", false);
                                GetComponent<Animator>().SetBool("IsJumping", true);
                                rb.velocity = new Vector2(rb.velocity.x, jumpForce);
                                PlaySoundEffect(0);
                                break;
                        }
                    }
                    else
                    {
                        Debug.Log("Not Mobile");
                        GetComponent<Animator>().SetBool("IsRunning", false);
                        GetComponent<Animator>().SetBool("IsJumping", true);
                        rb.velocity = new Vector2(rb.velocity.x, jumpForce);
                        PlaySoundEffect(0);
                    }
                }
                else
                {
                    if (jump)
                    {
                        if (SystemInfo.deviceType == DeviceType.Handheld)
                        {
                            Touch touch = Input.GetTouch(0);
                            switch (touch.phase)
                            {
                                case TouchPhase.Began:
                                    Debug.Log("DOUBLE JUMP");
                                    GetComponent<Animator>().SetBool("IsRunning", false);
                                    GetComponent<Animator>().SetBool("IsJumping", true);
                                    rb.velocity = new Vector2(rb.velocity.x, jumpForce);
                                    PlaySoundEffect(0);
                                    jump = false;
                                    break;
                            }
                        }
                        else
                        {
                            Debug.Log("DOUBLE JUMP");
                            GetComponent<Animator>().SetBool("IsRunning", false);
                            GetComponent<Animator>().SetBool("IsJumping", true);
                            rb.velocity = new Vector2(rb.velocity.x, jumpForce);
                            PlaySoundEffect(0);
                            jump = false;
                        }
                    }
                }

            }
        }
    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.collider.tag == "ground")
        {
            jump = false;
            GetComponent<Animator>().SetBool("IsRunning", true);
            GetComponent<Animator>().SetBool("IsJumping", false);
        }
    }
    private void OnCollisionStay2D(Collision2D collision)
    {
        if (collision.collider.tag == "ground")
        {
            isGrounded = true;
        }
    }
    private void OnCollisionExit2D(Collision2D collision)
    {
        if (collision.collider.tag == "ground")
        {
            isGrounded = false;
        }
    }

    public void PlaySoundEffect(int index)
    {
        aS.PlayOneShot(clipsSound[index]);
    }

}
