const typeSelect = document.querySelector("#type");
const pathInput = document.querySelector("#path-input");
const osSelect = document.querySelector("#os");
const osFormGroup = document.querySelector("#os-form-group");

function updateForm() {
  if (typeSelect.value === "File monitor") {
    osFormGroup.classList.remove("d-none");
  } else {
    osFormGroup.classList.add("d-none");
  }
}

typeSelect.addEventListener("change", updateForm);

updateForm();
