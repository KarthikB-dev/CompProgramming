from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
      # Trusts: int -> list[int] of people they trust
      # Trusted: int -> list[int] of people who trust that person
      # Person who has a trusts list of size 0 and a trusted list of size
      # n is the town judge
      trusts = {}
      trusted = {}
      people = set()

      if n == 1 and len(trust) == 0:
        return 1

      for a, b in trust:
        if a not in trusts:
          trusts[a] = []
        if b not in trusted:
          trusted[b] = []

        trusts[a].append(b)
        trusted[b].append(a)

        people.add(a)
        people.add(b)

      for person in people:
        if (person not in trusts) and (len(trusted[person]) == n - 1):
          return person

      return -1
