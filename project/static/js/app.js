var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(function ($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'static/partials/test.html',
      controller: 'testController'
    })
    .otherwise({
      redirectTo: '/'
    });
});