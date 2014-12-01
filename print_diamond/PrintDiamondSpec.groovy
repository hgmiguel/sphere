/**
Given a letter print a diamond starting with 'A' 
with the supplied letter at the widest point. 
For example: print-diamond 'E' prints
    A
   B B
  C   C
 D     D
E       E
 D     D
  C   C
   B B
    A
*/
package com.hgmiguel.test
@Grab('org.spockframework:spock-core:0.7-groovy-2.0')
//I need this hack
import spock.lang.Specification

class PrintDiamondSpec extends Specification {
  def "print a pattern"() {
    given:
    def diamond = new Diamond(input)
    expect:
    def out = diamond.print()
    out == output
    where:
    input || output
     'A'  || 'A'
     'B'  || ' A '''+
             'B B' +
             ' A '
  }

}

@groovy.transform.Canonical
class Diamond {
  final A = 65
  String input

  def print() {
    'A'
  }
}

