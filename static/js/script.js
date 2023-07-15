//Call jQuery before below code
$('.main-btn').click(function() {
  $('.search-description').slideToggle(100);
});
$('.search-description li').click(function() {
  var target = $(this).html();
  var toRemove = 'By ';
  var newTarget = target.replace(toRemove, '');
  //remove spaces
  newTarget = newTarget.replace(/\s/g, '');
  $(".search-large").html(newTarget);
  $('.search-description').hide();
  $('.main-input').hide();
  newTarget = newTarget.toLowerCase();
  $('.main-' + newTarget).show();
});
$('#main-submit-mobile').click(function() {
  $('#main-submit').trigger('click');
});
$(window).resize(function() {
  replaceMatches();
});

function replaceMatches() {
  var width = $(window).width();
  if (width < 516) {
    $('.main-location').attr('value', 'City or postal code');
  } else {
    $('.main-location').attr('value', 'Search by city or postal code');
  }
};
replaceMatches();

function clearText(thefield) {
  if (thefield.defaultValue == thefield.value) {
    thefield.value = ""
  }
}

function replaceText(thefield) {
  if (thefield.value == "") {
    thefield.value = thefield.defaultValue
  }
}


function showProductImage() {
  const inputElement = document.getElementById("productURLInput");
  const url = inputElement.value;
  
  const imageContainer = document.getElementById("productImageContainer");
  imageContainer.innerHTML = "";

  const image = new Image();
  image.src = url;
  image.onload = function() {
    imageContainer.appendChild(image);
  };
  image.onerror = function() {
    // Handle image loading error, show a placeholder image, or display an error message
  };
}


function performSearch() {
  const searchQuery = document.getElementById("searchInput").value;
  const searchResultsContainer = document.getElementById("searchResults");
  
  // Clear previous search results
  searchResultsContainer.innerHTML = "";

  // Perform search using the search engine of your choice
  // Here, we are simply displaying the search query as the result
  const searchResult = document.createElement("p");
  searchResult.textContent = `Search Results for: ${searchQuery}`;
  searchResultsContainer.appendChild(searchResult);
}