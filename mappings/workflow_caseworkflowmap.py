<?php


if(isset($_GET['specific_workflow_case'])):


	$workflow_case_id = isset($_GET['workflow_case_id']) ? $fieldValidator->validate_field($_GET['workflow_case_id']) : "";

	$workflowworkflow_casemap_array = array();
	$workflow_case_array = array();
	$workflow_array = array();

	$query = $queryExecutor->execute($selectionObj->select_workflow_case($workflow_case_id));

	while($row = mysqli_fetch_array($query)):

		$workflow_case_id = $row['workflow_case_id'];
		$workflow_case_array[$workflow_case_id] = array();
		$workflow_case_array[$workflow_case_id]['workflow_case_id'] = $workflow_case_id;

		$key = $workflow_case_id;

		$dependent_query = $queryExecutor->execute($selectionObj->select_workflow_case_legacy_id($workflow_case_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$workflow_case_array[$key]['legacy_id'] = $row_col['legacy_id'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_workflow_case_name($workflow_case_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$workflow_case_array[$key]['name'] = $row_col['name'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_workflow_case_description($workflow_case_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$workflow_case_array[$key]['description'] = $row_col['description'];


		$secondary_query = $queryExecutor->execute($selectionObj->select_workflowworkflow_casemap_by_workflow_case($workflow_case_id));

		while($sec_row = mysqli_fetch_array($secondary_query)):

			$workflow_id = $sec_row['workflow_id'];
			$workflow_array[$workflow_id] = array();
			$workflow_array[$workflow_id]['workflow_id'] = $workflow_id;

			$sec_key = $workflow_id;

			$dependent_query = $queryExecutor->execute($selectionObj->select_workflow_name($workflow_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workflow_array[$sec_key]['name'] = $row_col['name'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_workflow_description($workflow_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workflow_array[$sec_key]['description'] = $row_col['description'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_workflow_number_of_steps($workflow_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workflow_array[$sec_key]['number_of_steps'] = $row_col['number_of_steps'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_workflow_status($workflow_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workflow_array[$sec_key]['status'] = $row_col['status'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_workflow_is_mandatory($workflow_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workflow_array[$sec_key]['is_mandatory'] = $row_col['is_mandatory'];

		endwhile;



	endwhile;


?>

<table cellspacing = "1" cellpadding = "0" align = "center" width = "100%" id = "workflowworkflow_casemap">
 <tr>
 <td colspan = "7">&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td colspan = "2"><a href="target_print.php?workflowworkflow_casemap&&workflow_case_id=<?= $workflow_case_id ?>" target="_blank" style="color:#00FF00;">Print PDF</a></td></tr>
 <tr class = "top_row">
 <td>&nbsp;&nbsp;#&nbsp;&nbsp;</td>
 <td>&nbsp;Workflow id&nbsp;</td>
 <td>&nbsp;Name&nbsp;</td>
 <td>&nbsp;Description&nbsp;</td>
 <td>&nbsp;Number of steps&nbsp;</td>
 <td>&nbsp;Status&nbsp;</td>
 <td>&nbsp;Is mandatory&nbsp;</td>
 <td>&nbsp;Workspace id&nbsp;</td>
 <td>&nbsp;&nbsp;Actions&nbsp;&nbsp;</td></tr>
 
<?php $i = 0; ?>


<?php  foreach($workflow_array as $workflow_key => $workflow_value): ?>
<?php $css_class = ($i+1)%2 == 0 ? "even_row" : "odd_row"; ?>


<tr>
	<td><?= ($i+1) ?></td>
	<td><?= $workflow_value['workflow_id'] ?></td>
	<td><?= $workflow_value['name'] ?></td>
	<td><?= $workflow_value['description'] ?></td>
	<td><?= $workflow_value['number_of_steps'] ?></td>
	<td><?= $workflow_value['status'] ?></td>
	<td><?= $workflow_value['is_mandatory'] ?></td>
	<td><?= $workflow_value['workspace_id'] ?></td>
	<td>

		<?php $id_string = $workflow_id; ?>

		<div id="update_workflow_<?= $id_string ?>" style="display:none" class="updates">
		<table border="0" align="center" class="overlay_contained_table">
		<tr>
			<td align="right">
			<div class="closebtn" id="close_circle" onclick="closeUpdateOverlay('update_workflow_<?= $id_string ?>');">&nbsp;&times;&nbsp;</div>
			</td>
		</tr>
		<tr><td><br /></td></tr>
		<tr>
			<td align="center">
			<fieldset style="width: 80%">
			<legend>workflow Information</legend>
			<?php update_workflow($queryExecutor, $selectionObj, $updateObj, $fieldValidator, $workflow_value['workflow_id']); ?>
			</fieldset>
			</td>
		</tr>
		<tr>
			<td><br /></td>
		</tr>
		</table>
		</div>


<?php

	$workflowworkflow_casemap_count = count_workflowworkflow_casemap($queryExecutor, $selectionObj);
	$mapping_link = "workflowworkflow_casemap.php?workflow&&workflow_id=".$workflow_value['workflow_id']."";
	$title = "workflowworkflow_casemap corresponding entries.";
	$label = "Wor.";
	get_mapping_mark_up($workflowworkflow_casemap_count, $mapping_link, $title, $label);



?>


	<label id="update_link_<?= $id_string ?>" onclick="showUpdate('update_<?= $id_string ?>');" style="cursor:pointer">
	<img src="images/icons/edit.png" width="15px" height="15px" title="edit entry" style="cursor:pointer" />
	</label> 
 &nbsp; 
	<?php 
		$link = "workflow.php?delete_Workflow&&workflow_id=".$workflow_value['workflow_id']."";
		$message = "";
	?>

	<?php showConfirmDeleteAction($id_string, $link, $message); ?>
	<label style="cursor:pointer" onclick="showDelete('delete_<?= $id_string ?>')">
	<img src="images/icons/delete.png" width="15px" height="15px" title="delete entry" />
	</label>
	</td>
<tr>
	<?php $i = ($i + 1); ?>
<?php endforeach; ?>
 <tr>
 <td colspan = "9"></td></tr></table>

<?php endif; ?>

