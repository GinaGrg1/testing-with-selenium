Feature: Test navigation between pages
  This feature test will test successfully navigating
  between the pages.

  Scenario: Homepage can goto Blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page

  Scenario: Blog can goto Homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the homepage
