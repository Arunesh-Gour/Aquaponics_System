var fetchdataurl;
var reloader;

function setColor (rowid, level) {
   if (level == 0) {
      $((rowid + " .safe")).css({
         "background-image": "radial-gradient(circle, #0AFC48aa 25%, #00000000 27%)",
      });
      $((rowid + " .danger")).css({
         "background-image": "radial-gradient(circle, #00000000 25%, #00000000 27%)",
      });
      $((rowid + " .toxic")).css({
         "background-image": "radial-gradient(circle, #00000000 25%, #00000000 27%)",
      });
   } else if (level == 1) {
      $((rowid + " .safe")).css({
         "background-image": "radial-gradient(circle, #00000000 25%, #00000000 27%)",
      });
      $((rowid + " .danger")).css({
         "background-image": "radial-gradient(circle, #FFF719aa 25%, #00000000 27%)",
      });
      $((rowid + " .toxic")).css({
         "background-image": "radial-gradient(circle, #00000000 25%, #00000000 27%)",
      });
   } else if (level == 2) {
      $((rowid + " .safe")).css({
         "background-image": "radial-gradient(circle, #00000000 25%, #00000000 27%)",
      });
      $((rowid + " .danger")).css({
         "background-image": "radial-gradient(circle, #00000000 25%, #00000000 27%)",
      });
      $((rowid + " .toxic")).css({
         "background-image": "radial-gradient(circle, #FE2A0Faa 25%, #00000000 27%)",
      });
   }
}

function fillvalues (data) {
   $("#TAN").text(data['TAN']);
   $("#Temperature").text(data['temperature']);
   $("#pH").text(data['pH']);
   $("#DO").text(data['DO']);
   $("#NO2").text(data['NO2']);
   $("#NO3").text(data['NO3']);
   $("#Water-Level").text(data['waterLevel']);
   $("#Unionized-NH3").text(data['unionizedNH3']);
   
   let tc = 0;
   let tc2 = 0;
   
   if (data['temperature'] >= 27.0 && data['temperature'] <= 29.0) {
      setColor('#TemperatureRow', 0);
      tc = 0;
   } else if ((data['temperature'] >= 18.0 && data['temperature'] < 27.0) ||
      (data['temperature'] > 29.0 && data['temperature'] <= 32.0)) {
      setColor('#TemperatureRow', 1);
      tc = 1;
   } else if (data['temperature'] < 18.0 || data['temperature'] > 32.0) {
      setColor('#TemperatureRow', 2);
      tc = 2;
   }
   
   if (data['pH'] >= 6.8 && data['pH'] <= 7.0) {
      setColor('#pHRow', 0);
      tc2 = 0;
   } else if ((data['pH'] >= 6.4 && data['pH'] < 6.8) ||
      (data['pH'] > 7.0 && data['pH'] <= 7.4)) {
      setColor('#pHRow', 1);
      tc2 = 1;
   } else if (data['pH'] < 6.4 || data['pH'] > 7.4) {
      setColor('#pHRow', 2);
      tc2 = 2;
   }
   
   if (tc == 0 && tc2 == 0) {
      if (data['TAN'] <= 1.0) {
         setColor('#TANRow', 0);
      } else if (data['TAN'] > 1.0) {
         setColor('#TANRow', 1);
      }
   } else if (tc == 0 && tc2 == 1) {
      setColor('#TANRow', 1);
   } else if (tc == 0 && tc2 == 2) {
      setColor('#TANRow', 2);
   } else if (tc == 1 && tc2 == 0) {
      setColor('#TANRow', 1);
   } else if (tc == 1 && tc2 == 1) {
      setColor('#TANRow', 1);
   } else if (tc == 1 && tc2 == 2) {
      setColor('#TANRow', 2);
   } else if (tc == 2 && tc2 == 0) {
      setColor('#TANRow', 2);
   } else if (tc == 2 && tc2 == 1) {
      setColor('#TANRow', 2);
   } else if (tc == 2 && tc2 == 2) {
      setColor('#TANRow', 2);
   }
   
   if (data['DO'] > 6.5) {
      setColor('#DORow', 0);
   } else if (data['DO'] >= 4.5 && data['DO'] <= 6.5) {
      setColor('#DORow', 1);
   } else if (data['DO'] < 4.5) {
      setColor('#DORow', 2);
   }
   
   if (data['NO2'] >= 0.5 && data['NO2'] <= 1.0) {
      setColor('#NO2Row', 0);
   } else if (data['NO2'] >= 0.1 && data['NO2'] < 0.5) {
      setColor('#NO2Row', 1);
   } else if (data['NO2'] < 0.1 || data['NO2'] > 1.0) {
      setColor('#NO2Row', 2);
   }
   
   if (data['NO3'] >= 10.0 && data['NO3'] <= 100.0) {
      setColor('#NO3Row', 0);
   } else if ((data['NO3'] >= 5.0 && data['NO3'] < 10.0) ||
      (data['NO3'] > 100.0 && data['NO3'] <= 450.0)) {
      setColor('#NO3Row', 1);
   } else if (data['NO3'] < 5.0 || data['NO3'] > 450.0) {
      setColor('#NO3Row', 2);
   }
   
   if (data['waterLevel'] >= 70.0 && data['waterLevel'] <= 80.0) {
      setColor('#WaterLevelRow', 0);
   } else if ((data['waterLevel'] >= 50.0 && data['waterLevel'] < 70.0) ||
      (data['waterLevel'] > 80.0 && data['waterLevel'] <= 85.0)) {
      setColor('#WaterLevelRow', 1);
   } else if (data['waterLevel'] < 50.0 || data['waterLevel'] > 85.0) {
      setColor('#WaterLevelRow', 2);
   }
   
   if (data['unionizedNH3'] >= 0.0 && data['unionizedNH3'] <= 0.3) {
      setColor('#UnionizedNH3Row', 0);
   } else if (data['unionizedNH3'] > 0.3 && data['unionizedNH3'] <= 0.5) {
      setColor('#UnionizedNH3Row', 1);
   } else if (data['unionizedNH3'] > 0.5) {
      setColor('#UnionizedNH3Row', 2);
   }
}

function hotreload () {
   $.post(
      fetchdataurl,
      {
         'tankName' : $("#TankSelection :selected").text(),
      },
      function(data, status) {
         fillvalues (data);
      }
   );
}

$(document).ready(function() {
   fetchdataurl = $("#fetchdataurl").val();
   reloader = setInterval(hotreload, 1000);
});
