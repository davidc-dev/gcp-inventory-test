# -*- coding: utf-8 -*- #
# Copyright 2025 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Resume command for Workbench Schedules."""

from googlecloudsdk.api_lib.colab_enterprise import util
from googlecloudsdk.api_lib.notebook_executor import schedules as schedules_util
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import parser_arguments
from googlecloudsdk.calliope import parser_extensions
from googlecloudsdk.command_lib.ai import endpoint_util
from googlecloudsdk.command_lib.notebook_executor import flags
from googlecloudsdk.core import log


_DETAILED_HELP = {
    'DESCRIPTION': """
        Resume a Workbench notebook execution schedule.
    """,
    'EXAMPLES': """
        To resume a paused schedule with id `my-schedule`, in region `us-central1`, run:

         $ {command} my-schedule --region=us-central1
    """,
}


@base.DefaultUniverseOnly
@base.ReleaseTracks(base.ReleaseTrack.BETA)
class Resume(base.UpdateCommand):
  """Resume a schedule."""

  @staticmethod
  def Args(parser: parser_arguments.ArgumentInterceptor):
    """Register flags for this command.

    Args:
      parser: The parser to register the flags with.
    """
    flags.AddResumeScheduleFlags(parser)

  def Run(self, args: parser_extensions.Namespace):
    """This is what gets called when the user runs this command.

    Args:
      args: The arguments that this command was invoked with.

    Returns:
      The API response from resuming the schedule.
    """
    release_track = self.ReleaseTrack()
    messages = util.GetMessages(self.ReleaseTrack())
    schedule_ref = args.CONCEPTS.schedule.Parse()
    region = schedule_ref.AsDict()['locationsId']
    with endpoint_util.AiplatformEndpointOverrides(
        version='BETA', region=region
    ):
      api_client = util.GetClient(release_track)
      schedules_service = (
          api_client.projects_locations_schedules
      )
      schedules_util.ValidateAndGetWorkbenchSchedule(
          args, messages, schedules_service
      )
      api_response = schedules_service.Resume(
          schedules_util.CreateScheduleResumeRequest(
              args, messages
          )
      )
      log.status.Print('Resumed schedule.')
      return api_response

Resume.detailed_help = _DETAILED_HELP
