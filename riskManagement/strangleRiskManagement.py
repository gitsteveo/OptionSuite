import enum
from riskManagement import riskManagement
from optionPrimitives import optionPrimitive

class StrangleManagementStrategyTypes(enum.Enum):
  HOLD_TO_EXPIRATION = 0
  CLOSE_AT_50_PERCENT = 1

class StrangleRiskManagement(riskManagement.RiskManagement):
  """This class handles risk management strategies for strangles."""

  def __init__(self, managementType: StrangleManagementStrategyTypes) -> None:
    self.__managementType = managementType

  def managePosition(self, currentPosition:optionPrimitive) -> bool:
    """Manages the current position in the portfolio.
    Managing the position means indicating whether the position should be removed from the portfolio. In addition, we
    could create another signalEvent here if we want to do something like roll the strategy to the next month.
    :param currentPosition: Current position in the portfolio.
    """
    if self.__managementType == StrangleManagementStrategyTypes.HOLD_TO_EXPIRATION:
      if currentPosition.getNumberOfDaysLeft() == 0:
        # Indicates that the options are expiring on this date.
        return True
    elif self.__managementType == StrangleManagementStrategyTypes.CLOSE_AT_50_PERCENT:
      # TODO(msantoro): Add supporting code here.
      return False
    else:
      raise NotImplementedError('No management strategy was specified or has not yet been implemented.')
    return False