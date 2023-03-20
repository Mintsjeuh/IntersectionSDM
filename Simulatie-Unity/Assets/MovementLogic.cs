using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;

namespace Assets
{
    public class MovementLogic
    {
        // West naar oost (links naar rechts)
        public Vector3 startPosition_81_TrafficLight = new Vector3(-9, -2, 0);
        public Vector3 endPosition_81_TrafficLight = new Vector3(9, -2, 0);

        // Oost naar west (rechts naar links)
        public Vector3 startPosition_21_TrafficLight = new Vector3(9,0,0);
        public Vector3 endPosition_21_TrafficLight = new Vector3(-9,0,0);

        // Zuid naar noord (beneden naar boven)
        public Vector3 startPosition_51_TrafficLight = new Vector3(1,-12,0);
        public Vector3 endPosition_51_TrafficLight = new Vector3(-1,8,0);

        // Noord naar zuid (boven naar beneden)
        public Vector3 startPosition_111_TrafficLight = new Vector3(-1,8,0);
        public Vector3 endPosition_111_TrafficLight = new Vector3(-1,-12,0);

    }
}
