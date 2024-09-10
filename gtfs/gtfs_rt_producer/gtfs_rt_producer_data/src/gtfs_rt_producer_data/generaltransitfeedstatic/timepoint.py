from enum import Enum

class Timepoint(Enum):
    """
    Indicates if arrival and departure times for a stop are strictly adhered to by the vehicle or if they are instead approximate and/or interpolated times. Symbols: APPROXIMATE - Times are considered approximate; EXACT - Times are considered exact.
    """
    APPROXIMATE = 'APPROXIMATE'
    EXACT = 'EXACT'

    __member_list = []

    @classmethod
    def from_ordinal(cls, ordinal: int|str) -> 'Timepoint':
        """
        Get enum member by ordinal

        Args:
            ordinal (int| str): The ordinal of the enum member. This can be an integer or a string representation of an integer.

        Returns:
            The enum member corresponding to the ordinal.
        """
        if ordinal is None:
            raise ValueError("ordinal must not be None")
        if not cls.__member_list:
            cls.__member_list = list(cls)
        if 0 <= int(ordinal) < len(cls.__member_list):
            return cls.__member_list[int(ordinal)]
        else:
            raise IndexError("Ordinal out of range for enum")

    @classmethod
    def to_ordinal(cls, member: 'Timepoint') -> int:
        """
        Get enum ordinal

        Args:
            member (Timepoint): The enum member to get the ordinal of.

        Returns:
            The ordinal of the enum member.
        """
        if not cls.__member_list:
            cls.__member_list = list(cls)
        return cls.__member_list.index(member)