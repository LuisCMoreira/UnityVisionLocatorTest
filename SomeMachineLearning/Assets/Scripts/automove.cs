using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class automove : MonoBehaviour
{
    private float topBound =5.0f;
    private float lowBound =-5.0f;
    private float rigthBound =10.0f;
    private float leftBound =-10.0f;

    private float speed = 10.0f;
    private float slowspeed = 7.0f;
    private float rotspeed = 50.0f;

    float randomAngle=0;

    bool updated=false; 

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Translate(Vector3.forward * Time.deltaTime * speed);

        if (transform.position.z > topBound)
        {

            transform.Rotate(Vector3.up * Time.deltaTime * rotspeed*randomAngle);
            speed = slowspeed;
            updated=false;

        } else if (transform.position.z < lowBound)
        {
            transform.Rotate(Vector3.up * Time.deltaTime * rotspeed*randomAngle);
            speed = slowspeed;
            updated=false;

        } else if (transform.position.x > rigthBound)
        {
           transform.Rotate(Vector3.up * Time.deltaTime * rotspeed*randomAngle);
           speed = slowspeed;
           updated=false;

        } else if (transform.position.x < leftBound)
        {
            transform.Rotate(Vector3.up * Time.deltaTime * rotspeed*randomAngle);
            speed = slowspeed;
            updated=false;

        } else if (!updated)
        {

            speed = 10.0f;
            
            randomAngle = (Random.Range(1, 3));

            if (randomAngle>1) 

                {randomAngle=-1;}
            else

                {randomAngle=1;}
            
            updated=true;
            Debug.Log("update to:" + randomAngle);

        }
    }
}
