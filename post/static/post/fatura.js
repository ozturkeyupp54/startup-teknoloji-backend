function showFields(type) {
    var bireyselFields = document.getElementById("bireyselFields");
    var kurumsalFields = document.getElementById("kurumsalFields");

    if (type === "bireysel") {
      bireyselFields.style.display = "block";
      kurumsalFields.style.display = "none";
    } else if (type === "kurumsal") {
      bireyselFields.style.display = "none";
      kurumsalFields.style.display = "block";
    }
  }